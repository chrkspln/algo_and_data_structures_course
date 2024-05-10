#   В пошуках Святого Грааля Iндiана Джонс зiткнувся з небезпечним випробуванням.
#   Йому потрiбно пройти крiзь прямокутний коридор, який складається з крихких плит.
#   Для заданого коридору, пiдрахуйте, скiльки всього iснує способiв пройти його успiшно.
#   Вхiднi данi
#   Вхiдний файл ijones .in складається з H + 1 рядкiв.
#   • Перший рядок мiстить два числа W i H, роздiленi пробiлом: W — ширина
#   коридору, H — висота коридору, 1 <= W, H <= 2000.
#   • Кожен з наступних H рядкiв мiстить слово довжиною W символiв, яке складається
#   з малих латинських лiтер вiд a до z.
#   Вихiднi данi
#   Вихiдний файл ijones .out повинен мiстити одне цiле число — кiлькiсть рiзних
#   шляхiв для виходу з коридору.

def read_input_file(file_name):
    input_matrix = []
    with open(file_name, "r") as file:
        W, H = map(int, file.readline().split())
        for line in range(H):
            row = list(map(int, file.readline().strip()))
            input_matrix.append(row)
    file.close()
    return input_matrix


def write_to_output_file(file_name, pathways_count):
    with open(file_name, "w") as file:
        file.write(str(pathways_count))
    file.close()
    return file
