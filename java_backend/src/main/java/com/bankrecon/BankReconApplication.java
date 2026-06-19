package com.bankrecon;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@org.springframework.scheduling.annotation.EnableAsync
public class BankReconApplication {

    public static void main(String[] args) {
        SpringApplication.run(BankReconApplication.class, args);
    }

}
