myHead :: [String] -> String
myHead ss = head ss

main = do
        contents <- readFile "input.txt"
        let rows = lines contents
        let first = myHead(rows)
        print(first)

