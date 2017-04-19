c ***************************************************************************
c ** FUEL UNIVERSES: Individual FE"s
c ===========================================================================
  100100     1  -10.5     -100 101 -20            u=100 $ Meat
  100101     2  -6.55     -102 105 21 -22         u=100 $ Cladding
  100102     2  -0.000001 -100 101 20 -21         u=100 $ Gas Gap
  100103     2  -6.55      102 -103 -22           u=100 $ Top Cap
  100104     2  -6.55     -105 106 -22            u=100 $ Bottom Cap
  100105     2  -6.55      103 -104 -23           u=100 $ Top Plug
  100106     2  -6.55     -106 107 -24            u=100 $ Bottom Plug
  100107     3  -0.777537  104                    u=100 $ Water Above Plug
  100108     3  -0.777537 -104 103 23             u=100 $ Water RadiallyTop
  100109     3  -0.777537 -107                    u=100 $ Water Below pin
  100110     3  -0.777537  107 -106 24            u=100 $ Water RadiallyBottom
  100111     3  -0.777537 -102 105 22             u=100 $ Water Around pin
c ***************************************************************************
c *Cell being filled
c ***************************************************************************
 1001     0         -10001 -40 41  fill=100 (  0.000000   0.000000  0.00)   $
 1002     2         -10002 10001 -41 42 imp:n=0  (  0.000000   0.000000  0.00)
c ===========================================================================

 10001       c/z     0.000000     0.000000   5.0
 10002       c/z     0.000000     0.000000   10.0
c ===========================================================================
c Cylinders **From VVER Fuel Specs PPT**
  20    cz 0.38              $ Fuel
  21    cz 0.3865            $ Cladding inner
  22    cz 0.455             $ Cladding outer
  23    cz 0.3               $ Top plug
  24    cz 0.25              $ Bottom Plug
c =========================================================================
c Cylinders for core boundaries
  30    cz 40                          $ Water boundary
c ===========================================================================
c Planes for core boundaries
  40    pz     926.8                   $ Water top
  41    pz    -226.8                   $ Water bottom
  40    pz     950.0                   $ GRAVE top
  41    pz    -250.0                   $ GRAVE bottom
c ===========================================================================
c Planes **Elevations from VVER Fuel Specs PPT**
  100 pz  116.8              $ Fuel top
  101 pz -125.7              $ Fuel bottom
  102 pz  125.75             $ Cladding top/Bottom of Top Cap
  103 pz  126.25             $ Top of Top cap/Bottom of Top Plug
  104 pz  126.8              $ Top of Top Plug
  105 pz -125.2              $ Cladding bottom/Top of Bottom Cap
  106 pz -125.7              $ Bottom of Bottom Cap/Top of Bottom Plug
  107 pz -126.8              $ Bottom of Bottom Plug
c ***************************************************************
c ROD SURFACES
c ***************************************************************
 11000         pz 126.8     $  Top of Fuel Rod
 22000         pz -126.8    $  Bottom of Fuel Rod
c ***************************************************************
c Hexagonal SURFACES ALL FUEL ASSEMBLY DEFS
c ***************************************************************
c ===========================================================================
c Cylinders for core boundaries
  305   cz 40                          $ Water boundary
c ===========================================================================
c Planes for core boundaries
  505   pz     926.8                   $ Water top
c ***************************************************************
c ***************************************************************

mode  n
kcode 100000 1.500000 30 250 300000
c ***************************************************************
c MATERIAL CARDS
c ***************************************************************
c FUEL for neutron transport (by mass fraction)
c (only U-235, U-238) rho = 10.970 g/cc
m1    92235.60c -0.05000 $ U-235 and mass fraction
      92238.60c -0.95000 $ U-238 and mass fraction
c ==============================================================
c Cladding E-110 Zr(98.78)+Nb(1.00)+O(0.10)+Fe(0.05)+Ni(0.02)
c +Cr(0.02)+C(0.02)+Hf(0.01) [w %]
c **From VVER440.pdf**
c Density: 6.55 g/cc
m2     40000.42c    -0.9878 $ Zr
       41093.80c    -0.01   $ NB
       8016.70c     -0.001  $ O
       26000.42c    -0.0005 $ Fe
       28000.42c    -0.0002 $ Ni
       24000.42c    -0.0002 $ Cr
       6000.70c     -0.0002 $ C
       72000.42c    -0.0001 $ Hf
c ===============================================================
c Moderator (H2O (99.70)+H3BO3 (0.30)) [w %]
c Density: 0.777537g/cc ** From VVER 440.pdf**
m3    1001.70c   -0.063116 $ H
      8016.70c   -0.80149  $ O
      5010.70c   -0.135394 $ B
imp:n             1            1        11r       $
c ***************************************************************************
c Source cards
c ***************************************************************************
c SOURCE DISTRIBUTED ACROSS THE CORE VOLUME
sdef ERG=D1 POS=0 0 0 AXS=0 0 1 RAD=D2 EXT=D3
sp1 -3
si2 0 1.50            $ radius of the active region
si3 -126 117    $ height of the active region
c ************************* TALLY SPECIFICATION ********************************
c Flux average tally for active fuel region of all 85 elements
f4:n  100100
f7:n  100100