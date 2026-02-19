FROM node:24.13.1-alpine AS development-dependencies-env
RUN corepack enable && corepack prepare pnpm@10.24.0 --activate
COPY . /app
WORKDIR /app
RUN pnpm install --frozen-lockfile

FROM node:24.13.1-alpine AS production-dependencies-env
RUN corepack enable && corepack prepare pnpm@10.24.0 --activate
COPY ./package.json pnpm-lock.yaml /app/
WORKDIR /app
RUN pnpm install --frozen-lockfile --prod

FROM node:24.13.1-alpine AS build-env
RUN corepack enable && corepack prepare pnpm@10.24.0 --activate
COPY . /app/
COPY --from=development-dependencies-env /app/node_modules /app/node_modules
WORKDIR /app
RUN pnpm run build

FROM node:24.13.1-alpine
RUN corepack enable && corepack prepare pnpm@10.24.0 --activate
COPY ./package.json pnpm-lock.yaml /app/
COPY --from=production-dependencies-env /app/node_modules /app/node_modules
COPY --from=build-env /app/build /app/build
WORKDIR /app
CMD ["pnpm", "run", "start"]
