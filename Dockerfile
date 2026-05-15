FROM alpine:3.20
LABEL org.opencontainers.image.title="tcl-stakeholder"
LABEL org.opencontainers.image.description="Deterministic Tcl stakeholder CLI"
RUN apk add --no-cache tcl python3
WORKDIR /app
COPY . /app
RUN python3 scripts/validate_scaffold.py
ENTRYPOINT ["tclsh", "bin/tcl-stakeholder"]
CMD ["--list-values", "--output-format", "json"]
