from PIL import Image
import numpy as np
# Open image
image = Image.open('image.jpg')

def truncate(x):
    '''makes sure returned value is between 0 and 255'''
    return min(255, max(0, x))
# Filter
def filter(image):
    # Get image dimesions
    width, height = image.size

    # Create a white RGB image
    new_image = Image.new("RGB", (width, height), "white")

    # # Filter magic happens here
    # # Anh xam thong thuong
    # for x in range(width):
    #     for y in range(height):
    #         # Get original pixel colors
    #         r, g, b = image.getpixel((x, y))
    #
    #         # New pixel colors
    #         r_ = g_ = b_ = (r + g + b) / 3
    #
    #         # Change new pixel
    #         new_pixel = (int(r_), int(g_), int(b_))
    #         new_image.putpixel((x, y), new_pixel)

    # # Anh xam co do sang la trung binh của anh
    # for x in range(width):
    #     for y in range(height):
    #         r, g, b = image.getpixel((x, y))
    #
    #         r_ = g_ = b_ = 0.299 * r + 0.587 * g + 0.114 * b
    #
    #         new_pixel = (int(r_), int(g_), int(b_))
    #         new_image.putpixel((x, y), new_pixel)

    # # Do sang
    # for x in range(width):
    #     for y in range(height):
    #         r, g, b = image.getpixel((x, y))
    #         d = 10 # 0 den 255
    #         # d is the brightness increase
    #         r_ = truncate(r + d)
    #         g_ = truncate(g + d)
    #         b_ = truncate(b + d)
    #
    #         new_pixel = (int(r_), int(g_), int(b_))
    #         new_image.putpixel((x, y), new_pixel)

    # # # Tuong phan
    # data = np.array(image)
    # # Calculate average brightness
    # μ = np.mean(data, axis=2)
    # μ_mean = μ.mean()
    # # Calculate factor
    # beta = 200 # 0 den 255
    # if beta == 255:
    #     alpha = np.infty
    # else:
    #     alpha = (255 + beta) / (255 - beta)
    # for x in range(width):
    #     for y in range(height):
    #         r, g, b = image.getpixel((x, y))
    #
    #         r_ = truncate(alpha * (r - μ_mean) + μ_mean)
    #         g_ = truncate(alpha * (g - μ_mean) + μ_mean)
    #         b_ = truncate(alpha * (b - μ_mean) + μ_mean)
    #
    #         new_pixel = (int(r_), int(g_), int(b_))
    #         new_image.putpixel((x, y), new_pixel)

    # # Do bao hoa mau sac
    # # Calculate factor
    # beta = 240 # 0 den 255
    # if beta == 255:
    #     alpha = np.infty
    # else:
    #     alpha = (255 + beta) / (255 - beta)
    #
    # for x in range(width):
    #     for y in range(height):
    #         r, g, b = image.getpixel((x, y))
    #
    #         μ = (r + g + b) / 3
    #
    #         r_ = truncate(alpha * (r - μ) + μ)
    #         g_ = truncate(alpha * (g - μ) + μ)
    #         b_ = truncate(alpha * (b - μ) + μ)
    #
    #         new_pixel = (int(r_), int(g_), int(b_))
    #         new_image.putpixel((x, y), new_pixel)

    # # hieu chinh he mau do hoa
    # for x in range(width):
    #     for y in range(height):
    #         r, g, b = image.getpixel((x, y))
    #         gamma = 0.9 # 0 den 1
    #         r_ = 255 * (r / 255) ** gamma
    #         g_ = 255 * (g / 255) ** gamma
    #         b_ = 255 * (b / 255) ** gamma
    #
    #         new_pixel = (int(r_), int(g_), int(b_))
    #         new_image.putpixel((x, y), new_pixel)

    # # # Lam mo
    # Load image pixels
    data = np.array(image)
    # Half kernel size
    a = 2 # lon hon 0
    for x in range(width):
        for y in range(height):
            # min and max are used for edge pixels
            x_start = max(x - a, 0)
            y_start = max(y - a, 0)

            x_end = min(x + a + 1, width)
            y_end = min(y + a + 1, height)

            # Array with all pixels inside square
            square = data[y_start:y_end, x_start:x_end]

            # We take their average
            r_, g_, b_ = square.mean(axis=(0, 1))

            new_pixel = (int(r_), int(g_), int(b_))
            new_image.putpixel((x, y), new_pixel)


    return new_image



# Show result
new_image = filter(image)
new_image.show()

