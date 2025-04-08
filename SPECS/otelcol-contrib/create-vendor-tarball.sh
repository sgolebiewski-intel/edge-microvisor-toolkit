#!/usr/bin/bash

tag=$1

if [[ -z $tag ]]; then
    echo "This script requires the tag as an argument."
    exit 1
fi

set -euo pipefail

# transform tag into version
case $tag in
    *beta*)
        # v2.0.0-beta.1 -> 2.0.0~beta1
        temp=${tag#v}
        version=${temp/-beta./~beta}
        ;;
    *rc*)
        # v2.0.0-rc.1 -> 2.0.0~rc1
        temp=${tag#v}
        version=${temp/-rc./~rc}
        ;;
    *)
        # v2.0.0 -> 2.0.0
        version=${tag#v}
        ;;
esac

echo "Using tag: $tag"
echo "Using version: $version"

git -c advice.detachedHead=false clone --branch "$tag" --depth 1  https://github.com/open-telemetry/opentelemetry-collector-releases.git opentelemetry-collector-releases-"$version"
pushd opentelemetry-collector-releases-"$version"

# Install ocb tool and use it to generate source vendor tar from the manifest.yaml that aligns with the POA usage of collector
make ocb
ocb --skip-compilation=true --config=../otelcol-contrib-poa-manifest.yaml

mkdir -p otelcol-contrib-"$version"
mv _build otelcol-contrib-"$version"
cp LICENSE otelcol-contrib-"$version"
cp -a distributions/otelcol-contrib/* otelcol-contrib-"$version"
pushd otelcol-contrib-"$version"/_build
GOPROXY='https://proxy.golang.org,direct' go mod vendor
popd
tar --exclude .git -czf otelcol-contrib-"$version"-vendored.tar.gz otelcol-contrib-"$version"
popd
mv opentelemetry-collector-releases-"$version"/otelcol-contrib-"$version"-vendored.tar.gz ./
rm -rf opentelemetry-collector-releases-"$version"
