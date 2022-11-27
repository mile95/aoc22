import System.IO


main = do
        contents <- readFile "input.txt"
        let d = lines contents
        print d 
