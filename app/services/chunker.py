class Chunker:
	def __init__(self, text: str, chunk_size: int = 2000, overlap_lines: int = 5):
		self.text = text
		self.chunk_size = chunk_size
		self.overlap_lines = overlap_lines

	def create_chunks(self) -> list[str]:
		
		text = self.text.replace("\r\n", "\n").replace("\r", "\n")

		lines = text.split("\n")

		chunks = []
		current_chunk_lines = []
		current_chunk_size = 0

		# Loop through the lines of the text
		for line in lines:

			line_with_newline = line + "\n"
			line_size = len(line_with_newline)

			# If adding the line to the chunk will exceed chunk size, create chunk
			if current_chunk_size + line_size > self.chunk_size:
				chunk_text = "".join(current_chunk_lines)
				chunks.append(chunk_text)

				# Fill state variables for next chunk with overlap
				current_chunk_lines = current_chunk_lines[-self.overlap_lines:]
				current_chunk_size = sum(len(l) for l in current_chunk_lines)

				# Need to add the line which triggered chunk creation to new chunk
				current_chunk_lines.append(line_with_newline)
				current_chunk_size += line_size
			else:
				# Add lines to the chunk and increase size
				current_chunk_lines.append(line_with_newline)
				current_chunk_size += line_size
			
		if current_chunk_lines:
			chunk_text = "".join(current_chunk_lines)
			chunks.append(chunk_text)

		return chunks