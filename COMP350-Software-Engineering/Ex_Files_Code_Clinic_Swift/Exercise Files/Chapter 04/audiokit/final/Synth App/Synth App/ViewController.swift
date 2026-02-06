//
//  ViewController.swift
//  Synth App
//
//  Created by Todd Perkins on 4/20/18.
//  Copyright © 2018 Todd Perkins. All rights reserved.
//

import UIKit
import AudioKit

class ViewController: UIViewController {
    var oscillator = AKOscillator()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        updateSound(pos: touches.first!.location(in: self.view))
    }
    
    override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
        
    }
    
    override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
        updateSound(pos: touches.first!.location(in: self.view))
    }
    
    func updateSound(pos:CGPoint) {
        
    }
}

