# Use the official Node.js image.
# https://hub.docker.com/_/node
FROM node:22-alpine

# Install FFmpeg for video processing
RUN apk add --no-cache ffmpeg

# Create and change to the app directory.
WORKDIR /usr/src/app

# Copy application dependency manifests to the container image.
# A wildcard is used to ensure both package.json AND package-lock.json are copied.
# Copying this separately prevents re-running npm install on every code change.
COPY package*.json ./

# Install production dependencies.
# If you add a package-lock.json speed your build by switching to 'npm ci'.
RUN npm ci

# Copy local code to the container image.
COPY . .

# Build the frontend assets.
RUN npm run build:android-release

# Ensure uploads directory exists
RUN mkdir -p uploads

# Expose the port the app listens on
EXPOSE 8080

# Run the web service on container startup.
# We use tsx to run the TypeScript server file.
CMD [ "npx", "tsx", "server.ts" ]
