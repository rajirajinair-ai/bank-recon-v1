package com.bankrecon;

import com.bankrecon.model.Bank;
import com.bankrecon.model.BankAccount;
import com.bankrecon.model.BankTransaction;
import com.bankrecon.model.Company;
import com.bankrecon.model.SourceTransaction;
import com.bankrecon.repository.BankAccountRepository;
import com.bankrecon.repository.BankRepository;
import com.bankrecon.repository.BankTransactionRepository;
import com.bankrecon.repository.CompanyRepository;
import com.bankrecon.repository.ReconciliationGroupRepository;
import com.bankrecon.repository.SourceTransactionRepository;
import com.bankrecon.service.TransactionService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.ActiveProfiles;

import java.math.BigDecimal;
import java.time.LocalDate;

import static org.junit.jupiter.api.Assertions.assertEquals;

@SpringBootTest
@ActiveProfiles("test")
class TransactionServiceTests {

    @Autowired
    private TransactionService transactionService;

    @Autowired
    private BankTransactionRepository bankTransactionRepository;

    @Autowired
    private SourceTransactionRepository sourceTransactionRepository;

    @Autowired
    private ReconciliationGroupRepository reconciliationGroupRepository;

    @Autowired
    private CompanyRepository companyRepository;

    @Autowired
    private BankRepository bankRepository;

    @Autowired
    private BankAccountRepository bankAccountRepository;

    @BeforeEach
    void setUp() {
        reconciliationGroupRepository.deleteAll();
        bankTransactionRepository.deleteAll();
        sourceTransactionRepository.deleteAll();
        bankAccountRepository.deleteAll();
        companyRepository.deleteAll();
        bankRepository.deleteAll();

        Company comp = new Company();
        comp.setCode("C1");
        comp.setName("Comp1");
        companyRepository.save(comp);

        Bank bank = new Bank();
        bank.setCode("B1");
        bank.setName("Bank1");
        bankRepository.save(bank);

        BankAccount acc = new BankAccount();
        acc.setAccountNumber("123");
        acc.setAccountType("Savings");
        acc.setBank(bank);
        acc.setCompany(comp);
        bankAccountRepository.save(acc);

        BankTransaction bt = new BankTransaction();
        bt.setBankAccount(acc);
        bt.setDate(LocalDate.now());
        bt.setAmount(new BigDecimal("100.00"));
        bt.setTransactionType("CR");
        bt.setUtr("RRN123");
        bt.setStatus("UNMATCHED");
        bankTransactionRepository.save(bt);

        SourceTransaction st = new SourceTransaction();
        st.setDate(LocalDate.now());
        st.setAmount(new BigDecimal("100.00"));
        st.setTransactionType("CR");
        st.setRrn("RRN123");
        st.setSourceType("UPI");
        st.setStatus("UNMATCHED");
        sourceTransactionRepository.save(st);
    }

    @Test
    void testAutoMatch() {
        String result = transactionService.autoMatchTransactions();
        assertEquals("Auto-matching completed. Matched: 1", result);

        assertEquals(1, reconciliationGroupRepository.findAll().size());
        assertEquals("MATCHED", bankTransactionRepository.findAll().get(0).getStatus());
        assertEquals("MATCHED", sourceTransactionRepository.findAll().get(0).getStatus());
    }
}
