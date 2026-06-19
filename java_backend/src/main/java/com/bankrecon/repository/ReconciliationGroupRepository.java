package com.bankrecon.repository;

import com.bankrecon.model.ReconciliationGroup;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ReconciliationGroupRepository extends JpaRepository<ReconciliationGroup, Long> {
}
