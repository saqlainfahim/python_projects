import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def all_videos(videos):
    print("\n")
    print("-" * 50)
    
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']} ")
    
    print("\n")
    print("-" * 50)

def add_video(videos):
    name = input("Name: ")
    time = input("Time: ")
    
    videos.append({'name': name, 'time': time})
    save_data(videos)

def update_video(videos):
    all_videos(videos)
    index = int(input("Enter choice: "))
    
    if 1 <= index <= len(videos):
        name = input("New name: ")
        time = input("New time: ")
        
        videos[index-1] = {'name':name, 'time': time}
        save_data(videos)
    else:
        print("Invalid choice !!!")

def delete_video(videos):
    all_videos(videos)
    index = int(input("Enter choice: "))
    
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data(videos)
    else:
        print("Invalid choice !!!")

def main():
    videos = load_data()
    
    while True:
        print("\n Simple Youtube Manager")
        print("1 -> List of all videos")
        print("2 -> Add video")
        print("3 -> Update video")
        print("4 -> Delete video")
        print("5 -> Exit")
        
        choice = input("Enter choice: ")

        match choice:
            case '1':
                all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice !!!")

if __name__ ==  "__main__":
    main() 