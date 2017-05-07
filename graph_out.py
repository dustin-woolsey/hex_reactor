

def main(fname):

    with open(fname) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]

    f4_start = 0
    f4_end = 0
    f4_fin = 0

    f7_start = 0
    f7_end = 0
    f7_fin = 0

    f4trigger = 0
    f7trigger = 0

    for index, line in enumerate(content):
        if 'tally type 4    track length estimate of particle flux.      units   1/cm**2' in line:
            print line
            index += 5
            print content[index]
            f4_start = index
            f4trigger=1


            pass

        if f4trigger == 1 and line == '' and index > f4_start:
            print content[index - 1]
            print content[index + 1]
            f4_end = index
            f4trigger += 1

            pass

        if f4trigger == 2 and '==========================================================' in line:

            f4_fin = index - 5
            f4trigger += 1
            print content[f4_fin - 1]
            pass


        if f4trigger == 3 and f7trigger ==0 and 'tally type 7    track length estimate of fission heating.    units   mev/gram' in line:
            print line
            index += 5
            print content[index]
            f7_start = index
            f7trigger = 1

            pass

        if f7trigger == 1 and f4trigger == 3 and line == '' and index > f7_start:
            print content[index - 1]
            print content[index + 1]
            f7_end = index
            f7trigger += 1

            pass

        if f7trigger == 2 and '==========================================================' in line:

            f7_fin = index - 5
            f7trigger += 1
            print content[f7_fin - 1]
            pass

        ##################################################################################





if __name__ == '__main__':
    main('fct5.o')