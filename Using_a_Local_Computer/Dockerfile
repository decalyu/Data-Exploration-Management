# Use Python 3.13 as the base image
FROM python:3.13

# Set the working directory inside the container
WORKDIR /app

# Install Jupyter Notebook and required Python libraries
RUN pip install --no-cache-dir jupyter pandas numpy matplotlib seaborn scikit-learn

# Copy all local project files into the container
COPY . .

# Run Jupyter Notebook on container startup
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

