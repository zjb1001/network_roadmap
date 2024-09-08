#!/bin/bash

# Check if running as root
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# Function to create a network namespace
create_netns() {
    echo "Creating network namespace: $1"
    ip netns add $1
}

# Function to list network namespaces
list_netns() {
    echo "Listing network namespaces:"
    ip netns list
}

# Function to execute a command in a network namespace
exec_in_netns() {
    echo "Executing '$2' in namespace $1"
    ip netns exec $1 $2
}

# Function to delete a network namespace
delete_netns() {
    echo "Deleting network namespace: $1"
    ip netns delete $1
}

# Main menu
while true; do
    echo "
    Network Namespace Manager
    1. Create a network namespace
    2. List network namespaces
    3. Execute command in a namespace
    4. Delete a network namespace
    5. Exit
    "
    read -p "Enter your choice: " choice

    case $choice in
        1)
            read -p "Enter namespace name: " ns_name
            create_netns $ns_name
            ;;
        2)
            list_netns
            ;;
        3)
            read -p "Enter namespace name: " ns_name
            read -p "Enter command to execute: " command
            exec_in_netns $ns_name "$command"
            ;;
        4)
            read -p "Enter namespace name to delete: " ns_name
            delete_netns $ns_name
            ;;
        5)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid option"
            ;;
    esac
done