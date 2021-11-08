def medians(nums1, nums2):
    list_ = sorted(nums1 + nums2)
    if len(list_) % 2 == 0:
        m = ((list_[len(list_) // 2 - 1] + list_[len(list_) // 2]) / 2)       
        return m
    else:
        m = list_[len(list_) // 2]
        return m
    print('Объединенный список - {}.'.format(list_))
    print('{} - медиана списка.'.format(list_))