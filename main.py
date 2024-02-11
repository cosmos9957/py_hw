# Алгоритм:
# 1. Вывод: приветствие, отображение перечня продуктов, клик для продолжения
# 2. Предложение узнать цену за 1 кг или сразу перейти к сбору корзины
# 2.1 Предложение узнать стоимость продукта за 1 кг
# 2.2 Предложение ввода продукта и его веса в граммах
# 2.3 Вывод итоговой стоимости за продукт
# 3. Предложение о продолжении наполнения корзины
# 4. Вывод итоговой цены за все продукты

# init vegetables
cucumber: str = "огурец"
tomato: str = "помидор"
potatoes: str = "картофель"
radish: str = "редис"
pumpkin: str = "тыква"
cabbage: str = "капуста"
bell_pepper: str = "перец сладкий"
onion: str = "лук"
zucchini: str = "кабачок"

print(
    f"\nЗдравствуйте!\nВ нашем магазине вы можете приобрести следующие виды продуктов:\n"
    f"\n{cucumber}\n{tomato}\n{potatoes}\n{radish}"
    f"\n{pumpkin}\n{cabbage}\n{bell_pepper}\n{onion}\n{zucchini}\n"
)
input('Для продолжения нажмите "Enter"...')
print(
    '\nЧтобы узнать цену продуктов за киллограмм напишите в поле ввода: "цена"\n'
    'Чтобы перейти к сбору продуктовой корзины напишите в поле ввода: "корзина"'
)

# init user selection
user_selection: str = input("Поле ввода: ")

# init price of vegetables
# TODO: Сделать словарь
cucumber_price: int = 113
tomato_price: int = 194
potatoes_price: int = 24
radish_price: int = 45
pumpkin_price: int = 18
cabbage_price: int = 64
bell_pepper_price: int = 138
onion_price: int = 13
zucchini_price: int = 78

product_name_to_price = {
    "cucumber_price": 113,
    "tomato_price": 194,
    "potatoes_price": 24,
    "radish_price": 45,
    "pumpkin_price": 18,
    "cabbage_price": 64,
    "bell_pepper_price": 138,
    "onion_price": 13,
    "zucchini_price": 78,
}

if (
    user_selection.lower() == "цена"
    or user_selection == '"цена"'
    or user_selection == "wtyf"
):
# TODO: if user_selection in ['цена', '"цена"'] ПРОЧИТАТЬ ПРО ОПЕРАТОР 'in'
    print("\nНапишите в поле ввода продукт, цену которого вы хотите узнать?")
    user_product_price: str = input(
        "Поле ввода: "
    )
# TODO: Сохранение ввода пользователя в переменную ПРОЧИТАТЬ ПОДРОБНЕЕ!
    if user_product_price.lower() == "огурец":
        print(str(cucumber_price) + " " + "рублей за кг")
    if user_product_price.lower() == "помидор":
        print(str(tomato_price) + " " + "рублей за кг")
    if user_product_price.lower() == "картофель":
        print(str(potatoes_price) + " " + "рублей за кг")
    if user_product_price.lower() == "редис":
        print(str(radish_price) + " " + "рублей за кг")
    if user_product_price.lower() == "тыква":
        print(str(pumpkin_price) + " " + "рублей за кг")
    if user_product_price.lower() == "капуста":
        print(str(cabbage_price) + " " + "рублей за кг")
    if user_product_price.lower() == "перец сладкий":
        print(str(bell_pepper_price) + " " + "рублей за кг")
    if user_product_price.lower() == "лук":
        print(str(onion_price) + " " + "рублей за кг")
    if user_product_price.lower() == "кабачок":
        print(str(zucchini_price) + " " + "рублей за кг")
# TODO: Добавить функционал возврата к меню для формирования корзины
elif (
    user_selection.lower() == "корзина"
    or user_selection == '"корзина"'
    or user_selection == "rjhpbyf"
):
    print(
        '\nНапишите в "поле ввода продукта" - продукт, который вы хотите добавить в корзину'
    )
    print('Напишите в "поле ввода веса" - вес продукта в граммах')
    user_product_basket: str = input("Поле ввода продукта: ")
    user_product_basket_weight = float(input("Поле ввода веса: "))
    # Вероятно, не всегда нужно присваивать тип переменной
    if user_product_basket.lower() == "огурец":
        total_price = cucumber_price / 1000 * user_product_basket_weight
        print(str(total_price) + " " + "рублей")
        offer_to_buyer: str = input("Может ещё что-нибудь? У нас скидки! ")
        if offer_to_buyer.lower() == "да":
            print("\nотлично!")
            # Дописать перевод к вводу юзером других данных
        elif offer_to_buyer.lower() == "нет":
            print("\nплохо!")
            # Дописать перевод к выводу юзера к итоговому подсчёту покупок в корзине
    if user_product_basket.lower() == "помидор":
        total_price = tomato_price / 1000 * user_product_basket_weight
        print(str(total_price) + " " + "рублей")
    if user_product_basket.lower() == "картофель":
        total_price = potatoes_price / 1000 * user_product_basket_weight
        print(str(total_price) + " " + "рублей")
    if user_product_basket.lower() == "редис":
        total_price = radish_price / 1000 * user_product_basket_weight
        print(str(total_price) + " " + "рублей")
    if user_product_basket.lower() == "тыква":
        total_price = pumpkin_price / 1000 * user_product_basket_weight
        print(str(total_price) + " " + "рублей")
    if user_product_basket.lower() == "капуста":
        total_price = cabbage_price / 1000 * user_product_basket_weight
        print(str(total_price) + " " + "рублей")
    if user_product_basket.lower() == "перец сладкий":
        total_price = bell_pepper_price / 1000 * user_product_basket_weight
        print(str(total_price) + " " + "рублей")
    if user_product_basket.lower() == "лук":
        total_price = onion_price / 1000 * user_product_basket_weight
        print(str(total_price) + " " + "рублей")
    if user_product_basket.lower() == "кабачок":
        total_price = zucchini_price / 1000 * user_product_basket_weight
        print(str(total_price) + " " + "рублей")
# TODO: Дописать else

# TODO: Ввести функционал при введении пользователем неверных команд
