import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.mensa.lu/en/mensa/online-iq-test/online-iq-test.html')
# driver.set_window_position(1900,300)
driver.maximize_window()

xpath_q1 = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[1]/tbody/tr[2]/td[3]/input'
q1 = driver.find_element('xpath', xpath_q1)
q1.send_keys('M')

xpath_q2 = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[1]/tbody/tr[3]/td[3]/input'
q2 = driver.find_element('xpath', xpath_q2)
q2.send_keys(15)

xpath_q3 = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[1]/tbody/tr[4]/td[3]/input'
q3 = driver.find_element('xpath', xpath_q3)
q3.send_keys('8')

xpath_q4 = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[1]/tbody/tr[5]/td[3]/input'
q4 = driver.find_element('xpath', xpath_q4)
q4.send_keys('6')

xpath_q5 = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[1]/tbody/tr[6]/td[3]/input'
q5 = driver.find_element('xpath', xpath_q5)
q5.send_keys('5')

xpath_q6 = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[1]/tbody/tr[7]/td[3]/input'
q6 = driver.find_element('xpath', xpath_q6)
q6.send_keys('4')

xpath_q7 = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[1]/tbody/tr[8]/td[3]/input'
q7 = driver.find_element('xpath', xpath_q7)
q7.send_keys('1')

xpath_q8 = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[1]/tbody/tr[9]/td[3]/input'
q8 = driver.find_element('xpath', xpath_q8)
q8.send_keys('2')


xpath_q9_c = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[2]/tbody/tr[2]/td[4]/input'
q9_c = driver.find_element('xpath', xpath_q9_c)
q9_c.click()

xpath_q10_b = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[2]/tbody/tr[4]/td[3]/input'
q10_b = driver.find_element('xpath', xpath_q10_b)
q10_b.click()

xpath_q11_c = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[2]/tbody/tr[6]/td[4]/input'
q11_c = driver.find_element('xpath', xpath_q11_c)
q11_c.click()

xpath_q12 = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[2]/tbody/tr[8]/td[5]/input'
q12 = driver.find_element('xpath', xpath_q12)
q12.click()

xpath_q13_d = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[2]/tbody/tr[10]/td[5]/input'
q13_d = driver.find_element('xpath', xpath_q13_d)
q13_d.click()

xpath_q14_c = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[2]/tbody/tr[12]/td[4]/input'
q14_c = driver.find_element('xpath', xpath_q14_c)
q14_c.click()

xpath_q15_c = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[2]/tbody/tr[14]/td[4]/input'
q15_c = driver.find_element('xpath', xpath_q15_c)
q15_c.click()

xpath_q16_d = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[2]/tbody/tr[16]/td[5]/input'
q16_d = driver.find_element('xpath', xpath_q16_d)
q16_d.click()

xpath_q17_b = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[2]/tbody/tr[18]/td[3]/input'
q17_b = driver.find_element('xpath', xpath_q17_b)
q17_b.click()

xpath_q18_a = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[2]/tbody/tr[20]/td[2]/input'
q18_a = driver.find_element('xpath', xpath_q18_a)
q18_a.click()



xpath_q19_a = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[2]/tbody/tr[2]/td[2]/input'
q19_a = driver.find_element('xpath', xpath_q19_a)
q19_a.click()
time.sleep()
q19_a.click()