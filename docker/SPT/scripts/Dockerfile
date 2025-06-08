FROM node:22.12.0-slim as builder
WORKDIR /app
COPY ./server/project/package.json /app/package.json
RUN npm i

FROM node:22.12.0 as builder-2 
WORKDIR /app
COPY ./server/ /app/server/
COPY --from=builder /app/node_modules/ /app/server/project/node_modules/
RUN cd /app/server/project && npm run build:release

FROM node:22.12.0 as runner
WORKDIR /app
RUN mkdir -p /app/scripts && mkdir -p /app/server/backup
COPY ./scripts/entrypoint.sh /app/scripts/
COPY --chown=1000:1000 --from=builder-2 /app/server/project/build/ /app/server/bin/
COPY --chown=1000:1000 --from=builder-2 /app/server/project/build/SPT_Data /app/server/backup/SPT_Data
EXPOSE 6969
USER 1000:1000
ENTRYPOINT /app/scripts/entrypoint.sh