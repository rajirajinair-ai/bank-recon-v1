package com.bankrecon.repository;

import com.bankrecon.model.SourceTransaction;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.List;
import java.math.BigDecimal;

@Repository
public interface SourceTransactionRepository extends JpaRepository<SourceTransaction, Long> {
    List<SourceTransaction> findByStatusAndAmountAndTransactionType(String status, BigDecimal amount, String transactionType);
}
