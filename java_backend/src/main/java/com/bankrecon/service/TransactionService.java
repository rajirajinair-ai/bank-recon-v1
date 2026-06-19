package com.bankrecon.service;

import com.bankrecon.model.BankTransaction;
import com.bankrecon.model.SourceTransaction;
import com.bankrecon.model.ReconciliationGroup;
import com.bankrecon.model.ReconciliationItem;
import com.bankrecon.repository.BankTransactionRepository;
import com.bankrecon.repository.SourceTransactionRepository;
import com.bankrecon.repository.ReconciliationGroupRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.ArrayList;

@Service
public class TransactionService {

    @Autowired
    private BankTransactionRepository bankTransactionRepository;

    @Autowired
    private SourceTransactionRepository sourceTransactionRepository;

    @Autowired
    private ReconciliationGroupRepository reconciliationGroupRepository;

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

                List<ReconciliationItem> items = new ArrayList<>();

                ReconciliationItem item1 = new ReconciliationItem();
                item1.setGroup(group);
                item1.setBankTransaction(bankTx);
                items.add(item1);

                ReconciliationItem item2 = new ReconciliationItem();
                item2.setGroup(group);
                item2.setSourceTransaction(match);
                items.add(item2);

                group.setItems(items);
                reconciliationGroupRepository.save(group);

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
