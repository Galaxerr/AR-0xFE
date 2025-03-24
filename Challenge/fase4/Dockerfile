# Dockerfile for fase4 (React app inside alternate-reality-0xfe)
FROM node:19

# Set the working directory to /app
WORKDIR /

# Copy the package.json and package-lock.json first for better layer caching
COPY alternate-reality-0xfe/package.json alternate-reality-0xfe/package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the app files into the container
COPY alternate-reality-0xfe ./

# Expose port 3000 (default React port)
EXPOSE 42069

# Run the React app when the container starts
CMD ["npm", "start"]
