.data
    GETA:           .asciiz "Dividend: "
    GETB:           .asciiz "Divisor: "
    QMSG:           .asciiz "Quotient = "
    RMSG:           .asciiz "Reminder = "
    NL:             .asciiz "\n"
    ERR:            .asciiz "Error\n"
    left:           .word 1
    right:          .word 1
    filename:       .asciiz "D:\\BTL\\INT1.BIN"  # Duong dan file chua du lieu
    buffer:         .space 8               # Dành 8 bytes cho 2 so 32-bit

.text
.globl main

# Quy dinh thanh ghi
# $a1 = Divisor
# $a2 = Quotient
# $a3 = Reminder
# $t4 = So bit = 31
# $s0 = A

main:
    # Mo file
    li $v0, 13               # Mo file 
    la $a0, filename         # Load dia chi cua file vao $a0
    li $a1, 0                # Flag: O_RDONLY 
    li $a2, 0                # Mode
    syscall                  # Goi he thong

    move $t0, $v0            # Luu mo ta file vao $t0

solve:
    # Doc 8 bytes (2 so 32-bit) tu file
    li $v0, 14               # Doc file
    move $a0, $t0            # Load mo ta cua file
    la $a1, buffer           # Dia chi bo dem de doc du lieu
    li $a2, 8                # So byte can doc
    syscall                  

    # Load du lieu vao thanh ghi
    la $t7, buffer
    lw $a1, 0($t7)           # Doc so Divisor tu bo dem
    lw $a2, 4($t7)           # Doc so Dividend tu bo dem
    
    # In so chia va so bi chia
    
    li $v0, 4
    la $a0, GETA 	     #In ra thong bao so thu nhat
    syscall

    li $v0, 1
    move $a0, $a2	     # Dividend
    syscall

    li $v0, 4
    la $a0, NL		     # Xuong dong
    syscall

    li $v0, 4
    la $a0, GETB	     # In ra thong bao so thu hai
    syscall

    li $v0, 1
    move $a0, $a1 	     # Divisor	
    syscall

    li $v0, 4
    la $a0, NL		     # Xuong dong
    syscall

    # Khoi tao
    li $t4, 31                  # $t4 = so bit = 31 
    addi $s0, $s0, 0            # A = 0

    # Xu ly ngoai le:
    beq $a1, $zero, zeroerror    # Chuong trinh bao loi khi chia cho so 0

    # STEP 1: Dich phai Q va A
loop:
    andi $t5, $a2, 1073741824   # Trich xuat msb-1 cua so bi chia (phan nguyen)
    srl $t5, $t5, 30            # Di chuyen msb-1 sang phai
    sll $a2, $a2, 1             # Dich trai Q 1 vi tri
    andi $a2, $a2, 2147483647   # Loai bo vi tri thu 32
    sll $s0, $s0, 1             # Dich trai A 1 vi tri
    or $s0, $s0, $t5            # Them msb cua Q vao A

    # STEP 2: A = A - M
    addi $s5, $s0, 0            # Luu tru A
    sub $s0, $s0, $a1           # A = A - M

    # STEP 3: So sanh msb cua A de lay lsb cua Q
    andi $t5, $s0, 2147483648   # Lay msb cua A
    beq $t5, $zero, cond1       # Neu A[msb] = 0, nhay den cond1
    j cond2                     # Neu A[msb] = 1, nhay den cond2

# cond1
cond1:  ori $a2, $a2, 1         # Neu A[msb] = 0, Q[lsb]=1
    j condover

# cond2
cond2: andi $a2, $a2, 4294967294 # Neu A[msb] = 1, Q[lsb]=0
    addi $s0, $s5, 0            # Khoi phuc A
    j condover

condover:
    addi $t4, $t4, -1           # n = n-1
    beq $t4, $zero, print_result     # Ket thuc phep chia 
    j loop			# Lap lai loop
# In thuong va so du
print_result:
    li $v0, 4                  
    la $a0, QMSG                    
    syscall                  
    move $a0, $a2                      
    li $v0, 1                        
    syscall                            
    li $v0, 4                          
    la $a0, NL                        
    syscall                          
    li $v0, 4                    
    la $a0, RMSG                    
    syscall                    
    move $a0, $s0                      
    li $v0, 1                          
    syscall                            
    li $v0, 4                          
    la $a0, NL                        
    syscall

# Ket thuc chuong trinh
exit_program:
    # Dong file
    li $v0, 16               # Dong file
    move $a0, $t0            # Mo ta file
    syscall                  
    li $v0, 10               # Ket thuc chuong trinh thuc thi
    syscall

zeroerror:
    # Thong bao loi chuong trinh
    li $v0, 4                            
    la $a0, ERR                          
    syscall
    j exit_program
