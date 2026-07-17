FROM mcr.microsoft.com/devcontainers/base@sha256:3612b800eaae8513e7dca54f21d2e4eda48eda57426f3746a78677f342ac7ee9

USER root

ARG MISE_VERSION=v2026.7.7
ARG MISE_SHA256=429f71e7e989908bf975aafac9066329c16e2d8fc7cd8e74fdf21dd6300ffe7c
RUN set -eux; \
    curl --proto '=https' --tlsv1.2 -fsSL "https://github.com/jdx/mise/releases/download/${MISE_VERSION}/mise-${MISE_VERSION}-linux-x64" -o /tmp/mise; \
    echo "${MISE_SHA256}  /tmp/mise" | sha256sum -c -; \
    install -m 0755 /tmp/mise /usr/local/bin/mise; \
    rm -f /tmp/mise

ENV PATH="/home/vscode/.local/share/mise/shims:${PATH}"

USER vscode
