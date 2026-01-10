#include <stdio.h>
#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    *returnSize = 2;
    int* result = (int*)malloc(sizeof(int) * 2);
    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[i] + nums[j] == target) {
                result[0] = i;
                result[1] = j;
                return result;
            }
        }
    }
    *returnSize = 0;
    return result;
}

int main(void) {
    int nums[] = {2, 7, 11, 15};
    int target = 9;
    int returnSize;

    int* indices = twoSum(nums, sizeof(nums) / sizeof(nums[0]), target, &returnSize);
    if (returnSize == 2) {
        printf("Indices: [%d, %d]\n", indices[0], indices[1]);
    } else {
        printf("No solution found\n");
    }

    free(indices);
    return 0;
}
