package com.bankrecon.controller;

import com.bankrecon.model.BankTransaction;
import com.bankrecon.repository.BankTransactionRepository;
import com.bankrecon.service.TransactionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/transactions")
public class TransactionController {

    @Autowired
    private BankTransactionRepository bankTransactionRepository;

    @Autowired
    private TransactionService transactionService;

    @GetMapping("/bank-transactions")
    public List<BankTransaction> getAllBankTransactions() {
        return bankTransactionRepository.findAll();
    }

    @PostMapping("/auto-match")
    public ResponseEntity<String> autoMatch() {
        String result = transactionService.autoMatchTransactions();
        return ResponseEntity.ok(result);
    }
}
