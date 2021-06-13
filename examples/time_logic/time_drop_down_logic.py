

# start_time = ''
# end_time = ''





# def get_data():
#     start_time = input("Enter from time: ").split()
#     end_time = input("Enter to time: ").split()
#     key_value_pair[start_time] = end_time

##### dart exaple lists
# void main() {
#   var from_time =  List<int>.generate(24, (i) => i);
#   print(from_time);
#  print(from_time.sublist(15));
# }

if __name__ == "__main__":

    def set_price(from_time, to_time, price):
        print("setting price")
        key_value_pair[from_time+'_to_'+to_time]= price


    do_continue = True
    is_continue='y'

    key_value_pair = {}

    from_time = [x for x in range(24)]
    to_time = [x for x in range(1, 24)]
    # get_data()
    start_time = input("Enter from time:{} -> ".format(from_time))
    end_time = input("Enter to time:{} -> ".format(to_time))
    amount = input("Enter amount: ")
    # key_value_pair[start_time] = end_time
    set_price(from_time=start_time, to_time=end_time, price=amount)
    while do_continue:
        is_continue = input("Do you want to continue: ")

        if is_continue == 'y':
            print(">>>>>>>>>> {}".format(start_time))
            print(">>>>>>>>>> {}".format(end_time))
            start_time = input("Enter from time from the list : {} ".format(from_time[int(end_time):]))
            end_time = input("Enter to time: {} ".format(to_time[int(end_time)+1:]))
            amount = input("Enter amount: ")
            set_price(from_time=start_time, to_time=end_time, price=amount)
        else:
            break
        print("looping to set price")
        # set_price()
print(key_value_pair)

# to_index = to_time.index(int(start_time[0]))
# print(to_time[to_index:])

