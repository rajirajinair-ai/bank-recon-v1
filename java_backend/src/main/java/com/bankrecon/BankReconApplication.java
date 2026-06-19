package com.bankrecon;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableAsync;

@SpringBootApplication
@EnableAsync
public class BankReconApplication {

    public static void main(String[] args) {
        SpringApplication.run(BankReconApplication.class, args);
    }

}
