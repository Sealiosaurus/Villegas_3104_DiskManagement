import matplotlib.pyplot as plt

def sstf_disk_scheduling(requests):
    current_track = requests[0]
    seek_sequence = [current_track]
    total_seek_time = 0

    print('\nSeek Order:')
    order_of_service = []

    while requests:
        closest_request = min(requests, key=lambda x: abs(x - current_track))
        order_of_service.append(closest_request)
        seek_sequence.append(closest_request)
        total_seek_time += abs(current_track - closest_request)
        current_track = closest_request
        requests.remove(closest_request)

    print(', '.join(map(str, order_of_service)))
    
    print('\nSeek Time Calculation:')
    for i in range(1, len(seek_sequence) - 1):
        print(f'({max(seek_sequence[i + 1], seek_sequence[i])} - {min(seek_sequence[i + 1], seek_sequence[i])})', end='')
        if i < len(seek_sequence) - 2:
            print(' + ', end='')
    print(f' = {total_seek_time}')

    y_labels = [f'ST{i}' for i in range(1, len(seek_sequence))]
    plt.plot(seek_sequence[1:], range(1, len(seek_sequence)), marker='o', linestyle='-', label='Seek Sequence')
    plt.xlabel('Tracks')
    plt.ylabel('Seek Time')
    plt.gca().invert_yaxis()
    plt.gca().xaxis.tick_top()
    plt.gca().xaxis.set_label_position('top') 
    plt.yticks(range(1, len(seek_sequence)), y_labels)
    for i, txt in enumerate(seek_sequence[1:]):
        plt.text(txt, i + 1 + 0.2, str(txt), ha='center', va='top')
    plt.grid(True)
    plt.title('SSTF Disk Scheduling')
    plt.legend()

    return total_seek_time

print('\nSSTF Disk Scheduling')
# disk_requests = [53, 98, 183, 37, 122, 14, 124, 65, 67]
# 53 98 183 37 122 14 124 65 67
input_str = input("Enter disk requests (space-separated): ")
disk_requests = list(map(int, input_str.split()))

total_seek_time = sstf_disk_scheduling(disk_requests)
print(f'Total Seek Time: {total_seek_time}')

plt.show()
