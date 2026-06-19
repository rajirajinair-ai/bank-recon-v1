package com.bankrecon.model;

import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(unique = true, nullable = false, length = 150)
    private String username;

    @Column(nullable = false, length = 128)
    private String password;

    @Column(length = 254)
    private String email;

    @ManyToOne
    @JoinColumn(name = "role_id")
    private Role role;
}
