#Problem 1
def manage_stage_changes(changes):
    schedule = []
    most_recent = []

    for s in changes:
        if s.lower() == "cancel":
            if schedule:
                most_recent.append(schedule.pop())
        elif s.lower() == "reschedule":
            if most_recent:
                schedule.append(most_recent.pop())
        else:
            schedule.append(s[-1])
    return schedule

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D",  "Cancel", "Cancel", "Reschedule"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 
print(manage_stage_changes(["Cancel", "Reschedule"]))
# init two stacks schedule and most recent
# iterate over the changes
# push to the stack if is schedule *
# if we get cancel pop the stack, and push to most_recent stack
# append most_recent back to stack
# stack
# O(N)
#O(N)
# sorted(requests, key =lamba x:x[0])  

# Problem 2
def process_performance_requests(requests):
    #create a list to store processed requests in correct order
    ret_list = []
    # sort requests list in descending order
    requests.sort(reverse=True)
    # loop through requests, add performances one by one to new list
    for i in requests:
        ret_list.append(i[1])
    return ret_list 
    # return list

print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))

def collect_festival_points(points):
    total = 0
    while points:
        total += points.pop()
    return total


print(collect_festival_points([5, 8, 3, 10])) 
print(collect_festival_points([2, 7, 4, 6])) 
print(collect_festival_points([1, 5, 9, 2, 8])) 
