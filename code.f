
	implicit none
	real*8 R,I,L,Bz_total,Br_total
	integer N,resz,resr

	real*8 z,rho,Bmag
	real*8 point(2)
	integer iz,ir

    	R = 0.0165d0
C radi de la bobina (m)
    	I = 1d0
C corrent (A)
    	N = 300     
C núm espires
    	L = 0.16d0
C longitud de la bobina (m)
    	resz =  50
    	resr =  21


	do iz=1,resz+1
	do ir=1,resr+1
    	  z = (-1.0d0+2.0d0*(dfloat(iz)-1.0d0)/dfloat(resz))*L 
    	  rho = (dfloat(ir)-1.0d0)/dfloat(resr)*2.0d0*R
	  point(1)=z
	  point(2)=rho
	  call biot_savart_loop(R, I, N, L, point,Bz_total,Br_total)
    	  Bmag = dsqrt(Br_total**2 + Bz_total**2)
          write(6,'(5f15.10)') z,rho,Bz_total,Br_total,Bmag
	enddo
	write(6,*)
	enddo

	stop
	end





	subroutine biot_savart_loop(R, I, N, L, point,Bz_total,Br_total)

	implicit none
	real*8 R,I,L,point(2)    
	integer N

	real*8 z0,r0,mu0,Bz_total,Br_total,dlong,pi,
     .         z_i,x,y,rx,ry,rz,dx,dy,dz,r_mag,phi
	real*8 r_vec(3),dL(3),dB(3)

	integer iphi,ij,nphi

	nphi = 100

	z0 = point(1)
	r0 = point(2)

	pi = 4.0d0*datan(1.0d0)
	mu0 = 4.0d0 * pi * 1.0d-7

	Bz_total = 0.0d0
	Br_total = 0.0d0
	dlong = 2.0d0 * pi * R / nphi

C   np.linspace(0, 2 * np.pi, 100)
	
	do ij=1,N
C for i in range(N):

          z_i = -L / 2.0d0 + dfloat(ij) * L / dfloat(N - 1)

	  do iphi = 0,nphi
	    phi = iphi * 2.0d0 * pi/nphi
            x = R * dcos(phi)
            y = R * dsin(phi)

            rx = r0 * dcos(0.0d0)  
            ry = r0 * dsin(0.0d0)
            rz = z0

            dx = rx - x
            dy = ry - y
            dz = rz - z_i
            r_vec(1) = dx
            r_vec(2) = dy
            r_vec(3) = dz

            r_mag = dsqrt(dx**2+dy**2+dz**2)

            if (r_mag .ne. 0.0d0) then
              dL(1) = - dsin(phi) * dlong
              dL(2) =   dcos(phi) * dlong
              dL(3) = 0.0d0
	      call producto_vectorial(dL,r_vec,dB)
              dB(1) = mu0 * I / (4.0d0 * pi) * dB(1) / r_mag**3
              dB(2) = mu0 * I / (4.0d0 * pi) * dB(2) / r_mag**3
              dB(3) = mu0 * I / (4.0d0 * pi) * dB(3) / r_mag**3
              Br_total=Br_total+dB(1)*dcos(0.0d0)+dB(2)*dsin(0.0d0)
              Bz_total=Bz_total+dB(3)
	    endif

	  enddo
	enddo

	return
	end



C
C
C
C
	subroutine producto_vectorial(a, b, c)
    	implicit none
    	real(8), intent(in)  :: a(3), b(3)
    	real(8), intent(out) :: c(3)

! Calculo del producto vectorial c = a x b
    	c(1) = a(2)*b(3) - a(3)*b(2)
    	c(2) = a(3)*b(1) - a(1)*b(3)
    	c(3) = a(1)*b(2) - a(2)*b(1)

	end subroutine producto_vectorial
