package com.bankrecon.repository;

import com.bankrecon.model.ReconciliationItem;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ReconciliationItemRepository extends JpaRepository<ReconciliationItem, Long> {
}
