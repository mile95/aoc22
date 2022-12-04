main = do
        contents <- readFile "input.txt"
        let rows = lines contents
        print(rows)

