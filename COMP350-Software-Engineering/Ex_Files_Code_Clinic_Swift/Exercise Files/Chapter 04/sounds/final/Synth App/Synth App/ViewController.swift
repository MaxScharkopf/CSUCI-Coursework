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
        oscillator.amplitude = 0.1
    }
    
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        updateSound(pos: touches.first!.location(in: self.view))
    }
    
    override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
        oscillator.stop()
    }
    
    override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
        updateSound(pos: touches.first!.location(in: self.view))
    }
    
    func updateSound(pos:CGPoint) {
        if AudioKit.output == nil {
            AudioKit.output = oscillator
            do {
                try AudioKit.start()
            } catch {
                print(error)
            }
        }
        
        if oscillator.isStopped {
            oscillator.start()
        }
        let yPercent = Double(pos.y / UIScreen.main.bounds.height)
        let xPercent = Double(pos.x / UIScreen.main.bounds.width)
        oscillator.frequency = yPercent * 880 + 440
        oscillator.amplitude = xPercent * 0.5 + 0.2
        view.backgroundColor = UIColor(hue: CGFloat(yPercent), saturation: CGFloat(xPercent), brightness: 1.0, alpha: 1.0)
    }
}

