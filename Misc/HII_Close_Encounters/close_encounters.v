//Designed for the Cyclone III FPGA Starter Board
//Reference manual found At https://cdrdv2-public.intel.com/654220/rm_ciii_starter_board.pdf
module close_encounters (buttons[3:0], cpu_reset_n, led[3:0], clk);
	input [3:0] buttons;
	input cpu_reset_n;
	input clk; //50 MHz
	output [3:0] led;
	
	reg [2:0] out = 0;
	
	assign led[2:0] = out;
	assign led[3] = slow_clk;
	
	wire [4:0] all_buttons;
	
	//Assigned in physical layout on board
	assign all_buttons[4:0] = {cpu_reset_n, buttons[0], buttons[1], buttons[2], buttons[3]};
	
	reg slow_clk = 0;
	reg [32:0] count = 0;
	always @(posedge clk) begin
		if(count < 24999999) begin
			count <= count + 1;
		end else begin
			count <= 0;
			slow_clk <= ~slow_clk;
		end
	end
	
	reg [7:0] state = 0;
	
	always @(posedge slow_clk) begin
		case (state)
			0: begin
				if(all_buttons[4:0] == 5'b11101) begin
					state <= 1;
					out <= 3'b110;
				end else begin
					state <= 0;
					out <= 3'b111;
				end
			end
			1: begin
				if(all_buttons[4:0] == 5'b11110) begin
					state <= 2;
					out <= 3'b101;
				end else begin
					state <= 0;
					out <= 3'b111;
				end
			end
			2: begin
				if(all_buttons[4:0] == 5'b11011) begin
					state <= 3;
					out <= 3'b100;
				end else begin
					state <= 0;
					out <= 3'b111;
				end
			end
			3: begin
				if(all_buttons[4:0] == 5'b01111) begin
					state <= 4;
					out <= 3'b011;
				end else begin
					state <= 0;
					out <= 3'b111;
				end
			end
			4: begin
				if(all_buttons[4:0] == 5'b10111) begin
					state <= 5;
					out <= 3'b010;
				end else begin
					state <= 0;
					out <= 3'b111;
				end
			end
			5: begin
				out <= 3'b111;
				state <= 6;
			end
			6: begin
				out <= 3'b100;
				state <= 7;
			end
			7: begin
				out <= 3'b110;
				state <= 8;
			end
			8: begin
				out <= 3'b101;
				state <= 9;
			end
			9: begin
				out <= 3'b011;
				state <= 10;
			end
			10: begin
				out <= 3'b001;
				state <= 11;
			end
			11: begin
				out <= 3'b111;
				state <= 12;
			end
			12: begin
				if(all_buttons[4:0] == 5'b11101) begin
					state <= 13;
					out <= 3'b110;
				end else begin
					state <= 0;
					out <= 3'b111;
				end
			end
			13: begin
				if(all_buttons[4:0] == 5'b11110) begin
					state <= 14;
					out <= 3'b101;
				end else begin
					state <= 0;
					out <= 3'b111;
				end
			end
			14: begin
				if(all_buttons[4:0] == 5'b10111) begin
					state <= 15;
					out <= 3'b100;
				end else begin
					state <= 0;
					out <= 3'b111;
				end
			end
			15: begin
				out <= 3'b111;
				state <= 16;
			end
			16: begin
				out <= 3'b100;
				state <= 17;
			end
			17: begin
				out <= 3'b110;
				state <= 18;
			end
			18: begin
				out <= 3'b001;
				state <= 19;
			end
			19: begin
				out <= 3'b000;
				state <= 19;
			end
		endcase
	end
	
endmodule

