import pandas as pd


def build_xml(path: str, file_name: str):
    df = pd.read_excel(path, converters={"O_PESEL":str,  'KOD TERYTORIALNY': str})
    df = df[["O_PESEL", 'KOD TERYTORIALNY', 'Z_PROBKA_DATA_POBRANIA']]
    df["Z_PROBKA_DATA_POBRANIA"] = df["Z_PROBKA_DATA_POBRANIA"].dt.date
    num_lines = sum(1 for line in open('template.txt'))

    with open('template.txt') as template:
        body = []
        head = [next(template) for x in range(3)]
        for position, line in enumerate(template):
            print(num_lines - 4)
            if position == num_lines - 4:
                tail = line
            else:
                body.append(line)

    output = open(file_name + ".xml", "w")
    for index, row in df.iterrows():
        if index == 0:
            for line in head:
                output.write(line)
            for line in body:
                if line.startswith('  <nfz:zestaw-wyk-bad-poz id'):
                    updated_line = line.replace('id-zest-wyk-bad-poz="1"', f'id-zest-wyk-bad-poz="{index}"')
                elif line.startswith('        <nfz:ident'):
                    updated_line = line.replace('id-osoby="61021207287"', f'id-osoby="{row[0]}"')
                elif line.startswith('        <nfz:adres'):
                    updated_line = line.replace('teryt="2861011"', f'teryt="{row[1]}"')
                elif line.startswith('      <nfz:wyk-badanie '):
                    updated_line = line.replace('data-wyk-badania="2021-12-01"', f'data-wyk-badania="{row[2]}"')
                else:
                    updated_line = line
                output.write(updated_line)
        elif index == len(df)-1:
            output.write(tail)
        else:
            for line in body:
                if line.startswith('  <nfz:zestaw-wyk-bad-poz id'):
                    updated_line = line.replace('id-zest-wyk-bad-poz="1"', f'id-zest-wyk-bad-poz="{index}"')
                elif line.startswith('        <nfz:ident'):
                    updated_line = line.replace('id-osoby="61021207287"', f'id-osoby="{row[0]}"')
                elif line.startswith('        <nfz:adres'):
                    updated_line = line.replace('teryt="2861011"', f'teryt="{row[1]}"')
                elif line.startswith('      <nfz:wyk-badanie '):
                    updated_line = line.replace('data-wyk-badania="2021-12-01"', f'data-wyk-badania="{row[2]}"')
                else:
                    updated_line = line
                output.write(updated_line)

    output.close()

def main():
    # print("ścieżka do pliku wejściowego")
    # input_path = input()
    # print("nazwa pliku wyjściowego")
    # output_name = input()
    input_path, output_name = "E:/PM OLSZTYN GRUDZIEŃ/01-05.12.2021-NFZ_EPOZ.xlsx", "aaa"
    build_xml(input_path, output_name)


if __name__=="__main__":
    path = "F:/PM OLSZTYN GRUDZIEŃ/01-05.12.2021-NFZ_EPOZ.xlsx"
    main()
