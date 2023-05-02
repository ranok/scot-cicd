FROM bitnami/minideb

RUN install_packages curl ca-certificates python3 python3-pip wget
RUN pip3 install requests
RUN useradd runner

RUN mkdir /gh && chown -R runner:runner /gh

USER runner

RUN mkdir -p /gh/actions-runner
RUN cd /gh/actions-runner && curl -o actions-runner-linux-x64-2.303.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.303.0/actions-runner-linux-x64-2.303.0.tar.gz && tar xzf ./actions-runner-linux-x64-2.303.0.tar.gz

USER root

RUN /gh/actions-runner/bin/installdependencies.sh

COPY entry.sh /entry.sh
COPY gen_token.py /gen_token.py
COPY prep_env.sh /prep_env.sh

USER runner

ENTRYPOINT ["/entry.sh"]