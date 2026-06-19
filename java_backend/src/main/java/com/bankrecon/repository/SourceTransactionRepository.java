package com.bankrecon.repository;

import com.bankrecon.model.SourceTransaction;
import org.springframework.data.jpa.repository.JpaRepository;
import java.math.BigDecimal;
import java.util.List;

public interface SourceTransactionRepository extends JpaRepository<SourceTransaction, Long> {
    List<SourceTransaction> findByStatusAndAmountAndTransactionType(String status, BigDecimal amount, String transactionType);
}
