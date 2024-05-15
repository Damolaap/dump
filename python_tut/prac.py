'''
print('This is a love calculator :)')
start_calc = input('Do you want to try the Love Calculator: yes/no ').lower()

if start_calc == 'yes':
    print('The love calculator is calculating your score...')
    name1 = input('What is your name? ').lower()
    name2 = input('what is your name? ').lower()
    #true love...

    t_cnt = (name1).count('t')
    r_cnt = (name1).count('r')
    u_cnt = (name1).count('u')
    e_cnt = (name1).count('e')

    l_cnt = (name2).count('l')
    o_cnt = (name2).count('o')
    v_cnt = (name2).count('v')
    e_cnt = (name2).count('e')

    true_cnt = int(t_cnt + r_cnt + u_cnt + e_cnt)
    love_cnt = int(l_cnt + o_cnt + v_cnt + e_cnt)
    cnt = int(str(true_cnt) + str(love_cnt))
    if cnt < 10 or cnt > 90:
        print('')
    elif cnt >= 40 or <= 50:
        print(f'Your score is {cnt}, you are coke and mentos')
    else:
        print(f'Your score is {cnt}')
elif start_calc == 'no':
    print('Goodbye')
else:
    print('invalid input')
'''

