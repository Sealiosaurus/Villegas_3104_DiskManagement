import matplotlib.pyplot as plt

def scan_disk_scheduling(requests, disk_size):
    current_track = requests[0]
    seek_sequence = [current_track]
    total_seek_time = 0

    print('\nSeek Order:')
    order_of_service = [current_track]

    sorted_requests = sorted(requests[1:])
    higher_requests = [x for x in sorted_requests if x > current_track]
    lower_requests = [x for x in sorted_requests if x <= current_track]

    while higher_requests:
        closest_request = min(higher_requests)
        order_of_service.append(closest_request)
        seek_sequence.append(closest_request)
        total_seek_time += abs(current_track - closest_request)
        current_track = closest_request
        higher_requests.remove(closest_request)

    order_of_service.append(disk_size - 1)
    seek_sequence.append(disk_size - 1)
    total_seek_time += abs(current_track - (disk_size - 1))
    current_track = disk_size - 1

    while lower_requests:
        closest_request = max(lower_requests)
        order_of_service.append(closest_request)
        seek_sequence.append(closest_request)
        total_seek_time += abs(current_track - closest_request)
        current_track = closest_request
        lower_requests.remove(closest_request)

    print(', '.join(map(str, order_of_service)))
    
    print('\nSeek Time Calculation:')
    for i in range(len(seek_sequence) - 1):
        print(f'({max(seek_sequence[i + 1], seek_sequence[i])} - {min(seek_sequence[i + 1], seek_sequence[i])})', end='')
        if i < len(seek_sequence) - 2:
            print(' + ', end='')
    print(f' = {total_seek_time}')
    
    y_labels = [f'ST{i + 1}' for i in range(len(seek_sequence))]
    plt.plot(seek_sequence, range(len(seek_sequence)), marker='o', linestyle='-', label='Seek Sequence')
    plt.xlabel('Tracks')
    plt.ylabel('Seek Time')
    plt.gca().invert_yaxis()
    plt.gca().xaxis.tick_top()
    plt.gca().xaxis.set_label_position('top') 
    plt.yticks(range(len(seek_sequence)), y_labels)
    for i, txt in enumerate(seek_sequence):
        plt.text(txt, i + 0.2, str(txt), ha='center', va='top')
    plt.grid(True)
    plt.title('SCAN Disk Scheduling')
    plt.legend()

    return total_seek_time

print('\nSCAN Disk Scheduling')
# disk_requests = [53, 98, 183, 37, 122, 14, 124, 65, 67]
# 53 98 183 37 122 14 124 65 67
input_str = input("Enter disk requests (space-separated): ")
disk_requests = list(map(int, input_str.split()))
disk_size = int(input("Enter disk size: "))

total_seek_time = scan_disk_scheduling(disk_requests, disk_size)
print(f'Total Seek Time: {total_seek_time}')
plt.show()
