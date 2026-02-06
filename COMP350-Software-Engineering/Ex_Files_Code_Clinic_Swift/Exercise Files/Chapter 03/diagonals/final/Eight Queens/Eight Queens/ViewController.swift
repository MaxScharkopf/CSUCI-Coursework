//
//  ViewController.swift
//  Eight Queens
//
//  Created by Todd Perkins on 3/19/18.
//  Copyright © 2018 Todd Perkins. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var q1: UIImageView!
    @IBOutlet weak var q2: UIImageView!
    @IBOutlet weak var q3: UIImageView!
    @IBOutlet weak var q4: UIImageView!
    @IBOutlet weak var q5: UIImageView!
    @IBOutlet weak var q6: UIImageView!
    @IBOutlet weak var q7: UIImageView!
    @IBOutlet weak var q8: UIImageView!
    var queens:[UIImageView]!
    var startPos:CGPoint!
    
    @IBOutlet weak var labelSolution: UILabel!
    var solutions:[[Int]] = []
    var index:Int = -1
    
    func permuteWirth(_ a: [Int], _ n: Int) {
        if n == 0 {
            if isSolution(a) {
                solutions.append(a)
            }
        } else {
            var a = a
            permuteWirth(a, n - 1)
            for i in 0..<n {
                a.swapAt(i, n)
                permuteWirth(a, n - 1)
                a.swapAt(i, n)
            }
        }
    }
    
    func isSolution(_ a:[Int]) -> Bool{
        var diagForward:Set<Int> = [] // forward /
        var diagBackward:Set<Int> = [] // back \
        for i in 0..<a.count {
            diagForward.insert(a[i] + i)
            diagBackward.insert(a[i] - i)
        }
        return (a.count == diagForward.count && a.count == diagBackward.count)
    }
    
    

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        queens = [q1,q2,q3,q4,q5,q6,q7,q8]
        startPos = q1.center
        let numbers = [0,1,2,3,4,5,6,7]
        permuteWirth(numbers, numbers.count - 1)
        
        nextSolution()
    }
    
    func placeQueens() {
        
    }
    
    @IBAction func nextSolution() {
        index += 1
        if(index >= solutions.count){
            index = 0
        }
        labelSolution.text = "Solution: \(index + 1)/\(solutions.count)"
        placeQueens()
    }

}

