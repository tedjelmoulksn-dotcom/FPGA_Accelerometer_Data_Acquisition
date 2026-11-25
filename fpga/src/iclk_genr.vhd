library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity iclk_genr is
    port (
        CLK100MHZ : in  std_logic;  -- 100 MHz
        clk_4MHz  : out std_logic   -- ~4 MHz généré
    );
end entity;

architecture rtl of iclk_genr is
    signal counter : integer range 0 to 24 := 0;
    signal clk_reg : std_logic := '1';
begin

    process(CLK100MHZ)
    begin
        if rising_edge(CLK100MHZ) then
            if counter = 12 then
                clk_reg <= not clk_reg;
            end if;

            if counter = 24 then
                clk_reg <= not clk_reg;
                counter <= 0;
            else
                counter <= counter + 1;
            end if;
        end if;
    end process;

    clk_4MHz <= clk_reg;

end architecture;
