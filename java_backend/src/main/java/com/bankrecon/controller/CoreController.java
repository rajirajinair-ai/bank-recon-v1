package com.bankrecon.controller;

import com.bankrecon.model.*;
import com.bankrecon.repository.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/core")
public class CoreController {

    @Autowired
    private BankRepository bankRepository;

    @Autowired
    private BankAccountRepository bankAccountRepository;

    @Autowired
    private BranchRepository branchRepository;

    @Autowired
    private DepartmentRepository departmentRepository;

    @GetMapping("/banks")
    public List<Bank> getAllBanks() {
        return bankRepository.findAll();
    }

    @PostMapping("/banks")
    public Bank createBank(@RequestBody Bank bank) {
        return bankRepository.save(bank);
    }

    @GetMapping("/bank-accounts")
    public List<BankAccount> getAllBankAccounts() {
        return bankAccountRepository.findAll();
    }

    @PostMapping("/bank-accounts")
    public BankAccount createBankAccount(@RequestBody BankAccount acc) {
        return bankAccountRepository.save(acc);
    }

    @GetMapping("/branches")
    public List<Branch> getAllBranches() {
        return branchRepository.findAll();
    }

    @GetMapping("/departments")
    public List<Department> getAllDepartments() {
        return departmentRepository.findAll();
    }
}
