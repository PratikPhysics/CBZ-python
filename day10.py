# Do not run this file "day10.py" 💀❌💀❌💀 (these are just notes)

#step 1 install docker in ec2 -------------------------------------------------------
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update





#Step 2  install the following----------------------------------------------------------
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin





#Step 3 Start docker-----------------------------------------------------------
systemctl start docker
systemctl enable docker


#step 4 install docker for python-------------------------------------------------

apt install python3-docker -y



# step 5 create .py files-----------------------------------------------------------

#1. Connecting to Docker

import docker

client = docker.from_env()
print(client.version())  # Get Docker version





#2. Pull a Docker Image

image = client.images.pull('nginx')
print("Pulled image:", image.tags)




#3. List Available Images
images = client.images.list()
for img in images:
    print(img.tags)





#4. Run a Container

container = client.containers.run("nginx", detach=True, ports={'80/tcp': 8080})
print("Container ID:", container.id)




#5. List Running Containers

for container in client.containers.list():
    print(container.name, container.status)





#6. Stop and Remove a Container

container = client.containers.get("container_id")  # Replace with actual ID
container.stop()
container.remove()
print("Container stopped and removed.")




#7. Build a Docker Image from a Dockerfile

image, logs = client.images.build(path=".", tag="my_custom_image")
for log in logs:
    print(log.get("stream", "").strip())  # Display build logs





#8. Execute a Command in a Running Container
container = client.containers.get("container_id")  # Replace with actual ID
exec_log = container.exec_run("echo Hello from inside the container")
print(exec_log.output.decode())





#9. Remove an Image

client.images.remove("nginx")
print("Image removed.")





# for self study 😎
'''Advanced: Automating with a Python Script 
You can automate Docker tasks using a Python script.
Example: A script to start an Nginx container if it is not already running.'''

import docker

client = docker.from_env()

# Check if container exists
container_name = "my_nginx"

existing_containers = client.containers.list(all=True, filters={"name": container_name})

if existing_containers:
    container = existing_containers[0]
    if container.status != "running":
        container.start()
        print(f"Started existing container: {container_name}")
    else:
        print(f"Container {container_name} is already running.")
else:
    # Run new container if it doesn't exist
    container = client.containers.run("nginx", name=container_name, detach=True, ports={'80/tcp': 8080})
    print(f"Started new container: {container_name}")