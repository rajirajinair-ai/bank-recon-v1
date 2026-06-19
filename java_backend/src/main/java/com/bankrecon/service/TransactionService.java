package com.bankrecon.service;

import com.bankrecon.model.BankTransaction;
import com.bankrecon.model.ReconciliationGroup;
import com.bankrecon.model.ReconciliationItem;
import com.bankrecon.model.SourceTransaction;
import com.bankrecon.repository.BankTransactionRepository;
import com.bankrecon.repository.ReconciliationGroupRepository;
import com.bankrecon.repository.ReconciliationItemRepository;
import com.bankrecon.repository.SourceTransactionRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
public class TransactionService {

    @Autowired
    private BankTransactionRepository bankTransactionRepository;

    @Autowired
    private SourceTransactionRepository sourceTransactionRepository;

    @Autowired
    private ReconciliationGroupRepository reconciliationGroupRepository;

    @Autowired
    private ReconciliationItemRepository reconciliationItemRepository;

    @Transactional
    public String autoMatchTransactions() {
        List<BankTransaction> unmatchedBankTxs = bankTransactionRepository.findByStatus("UNMATCHED");
        int matchedCount = 0;

        for (BankTransaction bankTx : unmatchedBankTxs) {
            List<SourceTransaction> potentialMatches = sourceTransactionRepository
                .findByStatusAndAmountAndTransactionType("UNMATCHED", bankTx.getAmount(), bankTx.getTransactionType());

            SourceTransaction match = null;
            for (SourceTransaction st : potentialMatches) {
                if (st.getRrn() != null && st.getRrn().equals(bankTx.getUtr())) {
                    match = st;
                    break;
                }
            }

            if (match != null) {
                ReconciliationGroup group = new ReconciliationGroup();
                group.setStatus("PREPARED");
                reconciliationGroupRepository.save(group);

                ReconciliationItem item1 = new ReconciliationItem();
                item1.setGroup(group);
                item1.setBankTransaction(bankTx);
                reconciliationItemRepository.save(item1);

                ReconciliationItem item2 = new ReconciliationItem();
                item2.setGroup(group);
                item2.setSourceTransaction(match);
                reconciliationItemRepository.save(item2);

                bankTx.setStatus("MATCHED");
                bankTransactionRepository.save(bankTx);

                match.setStatus("MATCHED");
                sourceTransactionRepository.save(match);

                matchedCount++;
            }
        }

        return "Auto-matching completed. Matched: " + matchedCount;
    }
}
