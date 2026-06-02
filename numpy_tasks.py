import numpy as np

print("--- Завдання 1 ---")
array1 = np.random.randint(-10, 11, size=(4, 4))
array2 = np.random.randint(-10, 11, size=(4, 4))
array3 = np.random.randint(-10, 11, size=(4, 4))
combined_array = np.stack((array1, array2, array3), axis=0)
print("Об'єднаний масив з новою віссю:\n", combined_array)
assert combined_array.shape == (3, 4, 4), "Розмір об'єднаного масиву повинен бути (3, 4, 4)"

print("\n--- Завдання 2 ---")
B = np.random.randint(1, 10, (2, 3, 4))
print("Оригінальний тривимірний масив B:\\n", B)
B_reshaped = B.reshape(6, 4)
print("Масив після зміни форми:\\n", B_reshaped)
B_flattened = B.flatten()
print("Одновимірний масив:\\n", B_flattened)

print("\n--- Завдання 3 ---")
C = np.random.randint(1, 10, (3, 3, 3))
print("Оригінальний масив C:\\n", C)
sum_axis0 = C.sum(axis=0)
print("Сума по осі 0:\\n", sum_axis0)
sum_axis1 = C.sum(axis=1)
print("Сума по осі 1:\\n", sum_axis1)
total_sum = C.sum()
print("Загальна сума елементів масиву:", total_sum)
