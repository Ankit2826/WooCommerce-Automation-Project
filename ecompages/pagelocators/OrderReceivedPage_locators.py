from selenium.webdriver.common.by import By


class OrderReceivedPage:
    msg_1 = (
        By.XPATH, '//p[@class = "woocommerce-notice woocommerce-notice--success woocommerce-thankyou-order-received"]')
    order_num = (By.XPATH, '//li[@class = "woocommerce-order-overview__order order"]/strong/text()')
    order_dt = (By.XPATH, '//li[@class="woocommerce-order-overview__date date"]/strong/text()')
    order_amt = (By.XPATH, '//span[@class="woocommerce-Price-amount amount"]/bdi/text()')
