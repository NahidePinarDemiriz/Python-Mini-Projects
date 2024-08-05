def merge(nums1, m, nums2, n):
    # nums1'in son elemanından başlayarak işlem yapacağız.
    last = m + n - 1

    # m ve n'den başlayarak sona doğru elemanları karşılaştırarak yerleştiriyoruz.
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1
        last -= 1

    # Eğer nums2'de hala eleman kaldıysa onları da nums1'e ekliyoruz.
    while n > 0:
        nums1[last] = nums2[n - 1]
        n -= 1
        last -= 1

# Örnek kullanım
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)  # [1, 2, 2, 3, 5, 6]
