# AHT21
Tutorial to create a temperature and humidity sensor using AHT21 and Raspberry Pi Zero W.

### Materials:
Raspberry Pi Zero WH (W= Wireless, H= Headers (already soldered on))

[RPi](https://www.amazon.com/Raspberry-Bluetooth-Compatible-Connector-headers/dp/B0CG99MR5W?crid=YN19MCMRYEC1&dib=eyJ2IjoiMSJ9.WEtUDQK3vhQkFbdhbEmfjWrj_9w6I2o00tTxnnLh9T8v7-Q9FfEwbd3aPnh53XCOjxdwvMByjlossEZ1C09VjkflufTdu0pRNFIFnekUCu0adQJX5nQh4ElQ9wNNi-DL-Q3xMKTX_HPr8TQzf7RGnhQQHzqC6pTR_GFXXKtxfP4bni95r93Z5g2F3ZNP_zS_KYKdld8jQgPP9FVbt6xnCznnPfGXeV6_T0t7BzsRcXBVR70CE2qHD10Yeg5-Nt3sz7_yWhvVnHepARwkwowbOIVOQ4I5bI_bCrN6n3VY8508R3fVTiV4f8fcn6lRuFHbSOagvTzI8TnONCw8My3Nu-NLqv8f2wCexAISXRFnCko.ZwAyMG__KfboHmyRSViGvPvxUDbDSHWUBs8Pgnxqoiw&dib_tag=se&keywords=raspberry%2Bpi%2Bzero%2Bw%2Bh&qid=1740175076&s=electronics&sprefix=raspberrry%2Bpi%2Bzero%2Bw%2B%2Celectronics%2C213&sr=1-1&th=1)

AHT21 Sensor (Adafruit Humidity Temperature Sensors; brand matters -> code library used)

[AHT21 Sensors](https://www.amazon.com/UMLIFE-Precision-Temperature-Measurement-Communication/dp/B0C6DZ8YZG?crid=6KT50QK4051T&dib=eyJ2IjoiMSJ9.--9iZK9wWnKNwOHjRBdEsnOgpCZcL0V3rZdXW3BneKrRRTUKEV-4xwqiwmOQcXmch-4LNY3CXhMJIaRsgw-YE19_9oPCNUY7Ei-HE64CkUylj3EjCKtYh_Ewwpkd2e4PKiR0iXhrnyx00EvZDfkZAt4KUFXIS3cTuvGOo9QetFUDjWsZ94TcpSM2i5d4UV6Em-8UmNdBAdzkmlJiSg_2t3JLrBuIkqaAguwdcGcRhc0.AL-HbH3saLZ-HQf68Wmw1_wA0j5UtVst3vJWOnykzqc&dib_tag=se&keywords=aht21%2Btemperature%2Bsensor&qid=1740175406&sprefix=AHT21%2Caps%2C204&sr=8-5&th=1)

Breadboard and Jumper Wires (female-male wires; need 4 wires to connect the sensors to the breadboard and RPi; any breadboard is fine)

[Breadboard/Wire Set](https://www.amazon.com/HUAREW-Breadboard-Jumper-Include-Points/dp/B09VKYLYN7?crid=2LV4G3OA5VBHV&dib=eyJ2IjoiMSJ9.ozHaOEz11CAJtB_xbZ27F-e75UuFDp5cGrPdMUK1I-X73Vhc0u1U3IKdbRw0Kn2lsugL24L49g8Us7f-gVrIUbJYOTo5f9XcpIZgNX2lYVgBHJNWRCf06lu8CKsz0uNLRE_UrM8SrzQXpSuyLy9J6Ol_aOHhAF9iOsc1MjEKr7ajN_xdOuw9zKelyJrTrpCoaNsXsZwXg1GpweQhkxVlkcce551PlK4-CNnuCrfSnss.UNmPV_krCkfU3wT4rHPr_wS87d90idZtb-0NkZFWOy4&dib_tag=se&keywords=breadboard+and+jumper+wires&qid=1740175667&sprefix=breadboard+and+jumper+wir%2Caps%2C202&sr=8-3)

Micro-USB Cable and USB Power Supply (any is fine)

[Micro-USB Cable](https://www.amazon.com/Charging-Transfer-Android-Trustable-MYFON/dp/B098DW7485?crid=2KGXKFFMHT4LZ&dib=eyJ2IjoiMSJ9.WR63mKTxAJQICRAe9uZ2APmoXscPxGk0W7TyUC7zUOepA-mpjv4JSKc1TkT1jRBtRmhycVZ-cl4f3JYFXJR7O3_LLi8tkEZYT5f7mRLzJFfMCqghjIbRt4eznJGgL9yjrhd1zb7qvKVPF-RDueImDUPlszzwvTUlVjFaRiWpCVwkkyDuAYS4zCI0-1Tmf3UU56BfcM_TKoSWlt88bGwOz5jYuJS3tRJJiZg0mCpGFHg.CrI8OwJtEzEehjiZbrl8bqo9uIz5VVNQopMxnrXjyEE&dib_tag=se&keywords=micro%2Busb&qid=1740176049&sprefix=micro%2Bus%2Caps%2C424&sr=8-4&th=1)
 | [Power Supply with Micro-USB](https://www.amazon.com/Bawofu-Supply-Charger-Adapter-Universal/dp/B0BSF3TB8P?crid=GUN3N529THFG&dib=eyJ2IjoiMSJ9.lYhV7VDm_2PdWXB38EVtA02ZZ7iTnEt0e1GHHrJR7H-A7YUYv8pu5nxWQ7iMlAVJMPfazuqkRkG1BzAlhpBj4AjYpgJcEcc16EPM8PTqiW1PBQR6Drh13yWa1on5Gw0jTePA4rHzNEF3PaHFvhK9I9OuBv8BXpHlIZpUg0alz7NwJFWD_JH4RpYLw4iHFJc9go3ukDCHMC6_hDzy22HaQ24OA6pjEWbc4NFmOJ38OWE.BmYW0u6zvDPYID3bANagd9w2uxxxoVkdTjy3aoZ5TI8&dib_tag=se&keywords=usb+power+supply+micro+usb&qid=1740176249&sprefix=usb+power+supply+micro+us%2Caps%2C195&sr=8-3)

Micro SD-Card (I used 16gbs)

[Micro SD-Card](https://www.amazon.com/Center-Memory-Adapter-Mobile-Storage/dp/B08HD83TFJ?crid=2BQCKLHXHA5EH&dib=eyJ2IjoiMSJ9.Uwx19gT9ffNa_idEUNhHLJndkVLmxwwGnyqGY6G1drtN2FIqpZ_wLSP502zU4lT5zjOn7B-wRiLJ6fMHJoWHX165Mj-_fy6-B2s90l42A_S-AtgFJkagv_ywZk8Ex1R8fuDYqfwqa3CWecMKt1EXu0eRoirFcVh3iZrlrp6LsC19x1RwCJnKUxmdas0dDScssYJNrI4B4kqLAXwkg6KeI4XM28WHZFKjpsGHCEmv0Ec.xecKIXm0zfVyXNANv6De-CHw-tlmf1NerkyQ6wCURds&dib_tag=se&keywords=micro+sd+card+16gb+microcenter&qid=1740176570&sprefix=micro+sd+card+16gb+microcente%2Caps%2C182&sr=8-1)

Micro SD-Card Reader/Adapter

[Adapter](https://www.amazon.com/Reader-Adapter-Camera-Memory-Wansurs/dp/B0B9QZ4W4Y?crid=1NRJQU9RFIEUX&dib=eyJ2IjoiMSJ9.aZ5CyI1seaCTFVUzT0NlJpD8dyQjzqiqAURiyClSNrH2BGRKFKbUrMzzF59pt43S0IFH3E6I00N6K6GSyrhpmx3imwonNx4xzcFtk9ZzN4DJMNFZl6cg6qMy5rCOA6W2LOXlkYWOTcdxbBAmjkMfaEBSL3PMtZakDS_UNtSwuSrGZeT5n0gP3ZLp572kA636_A4iDL-Rms6Z5qR8qW5fw_pHX3N3wMLKtk3T0xdtz6U.9WVDsjNrwOKz5CJDiLGtSr47cc6gQd7MSiG2myKHeTE&dib_tag=se&keywords=micro+sd+card+adapter&qid=1740176655&sprefix=micro+sd+card+adapt%2Caps%2C207&sr=8-4)

